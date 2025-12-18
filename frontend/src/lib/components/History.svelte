<script lang="ts">
	import { createCursor } from '$lib/utils/cursor';
	import Translation from './Translation.svelte';
	import { type Translation as Trans } from '$lib/sdk/types';
	import { getTranslations } from '$lib/sdk/sdk';
	import LazyLoading from './LazyLoading.svelte';
	import { tick } from 'svelte';
	import handler from '$lib/utils/handler';

	let { translations } = $props();

	type TranslationsState = {
		translations: Trans[];
	};

	const MAX_LOAD = 200;

	let count = $state(false);

	const translationState: TranslationsState = $state(translations ? translations : []);

	const loadMore = handler(async () => {
		const lastTranslation = translationState.translations[translationState.translations.length - 1];
		const cursor = createCursor(lastTranslation.id, lastTranslation.created_at);
		const data = await getTranslations({
			cursor: cursor,
			limit: 20
		});
		if (data?.translations && data.translations.length > 1) {
			let newLength = translationState.translations.length + data.translations.length;
			if (translationState.translations.length > MAX_LOAD) {
				const content = document.scrollingElement!;
				const previousScrollHeight = content.scrollHeight;
				const previousScrollTop = content.scrollTop;
				translationState.translations.splice(0, translationState.translations.length - MAX_LOAD);
				tick().then(() => {
					const newScrollHeight = content.scrollHeight;
					content.scrollTop = previousScrollTop - (previousScrollHeight - newScrollHeight);
					count = true;
					translationState.translations.push(...data.translations);
				});
				tick().then(() => {
					// Restore loadMore after DOM updates
					loadMore.restore();
				});
			} else {
				translationState.translations.push(...data.translations);
				tick().then(() => {
					// Restore loadMore after DOM updates
					loadMore.restore();
				});
			}
		} else {
			tick().then(() => {
				// Restore loadMore after DOM updates
				loadMore.restore();
			});
		}
	});

	const loadPrevious = handler(async () => {
		const content = document.scrollingElement;
		if (!content) return;
		const previousScrollHeight = content.scrollHeight;
		const previousScrollTop = content.scrollTop;
		const firstTranslation = translationState.translations[0];
		const cursor = createCursor(firstTranslation.id, firstTranslation.created_at);
		const data = await getTranslations({
			cursor: cursor,
			direction: 'prev',
			limit: 20
		});
		if (data && data.translations.length > 0) {
			translationState.translations.unshift(...data.translations.reverse());
			await tick();
			const newScrollHeight = content.scrollHeight;
			const deltaHeight = newScrollHeight - previousScrollHeight;
			content.scrollTop = previousScrollTop + deltaHeight;
			const currentLength = translationState.translations.length;
			if (currentLength > MAX_LOAD) {
				const gap = currentLength - MAX_LOAD;
				translationState.translations.splice(currentLength - gap, gap);
			}
			loadPrevious.restore();
		} else {
			count = false;
			loadPrevious.restore();
		}
	});
</script>

<div class="history" id="history">
	{#if count}
		<LazyLoading loadData={loadPrevious} />
	{/if}
	{#each translationState.translations as translation (translation.id)}
		<Translation {translation} />
	{/each}
	<LazyLoading loadData={loadMore.once} />
</div>

<style>
	.history {
		display: flex;
		flex: 1;
		flex-direction: column;
		align-items: center;
		gap: 50px;
		margin-top: 50px;
	}
</style>
