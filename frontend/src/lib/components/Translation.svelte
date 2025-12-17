<script lang="ts">
	import type { Translation } from '$lib/sdk/types';
	import { fade, scale } from 'svelte/transition';

	let { translation }: { translation: Translation } = $props();

	let isOpen = $state(false);

	const openModal = () => {
		isOpen = true;
	};

	const closeModal = () => {
		isOpen = false;
	};
</script>

<div class="translation-container" onclick={openModal}>
	<div class="langs">
		<div class="source-lang">{translation.source_lang}</div>
		<div class="target-lang">{translation.target_lang}</div>
	</div>
	<div class="translation">
		<div class="source-text truncate-text">{translation.source_text}</div>
		<div class="target-text truncate-text">{translation.target_text}</div>
	</div>
</div>

{#if isOpen}
	<div transition:fade={{ duration: 200 }} class="modal-overlay" onclick={closeModal}>
		<div
			transition:scale={{ duration: 200 }}
			class="translation-container"
			onclick={(e) => e.stopPropagation()}
		>
			<div class="langs">
				<div class="source-lang">{translation.source_lang}</div>
				<div class="target-lang">{translation.target_lang}</div>
			</div>
			<div class="translation">
				<div class="source-text">{translation.source_text}</div>
				<div class="target-text">{translation.target_text}</div>
			</div>
		</div>
	</div>
{/if}

<style>
	* {
		box-sizing: border-box;
	}

	.translation-container {
		display: flex;
		flex-direction: column;
		width: 1000px;
		background: white;
		border: 1px solid #c2cad3;
		border-radius: 10px;
		box-shadow: 0px 0px 20px 2px rgba(0, 0, 0, 0.08);
		overflow: hidden;
	}

	.translation {
		display: flex;
		flex: 1;
		padding: 18px;
	}

	.source-text {
		border-right: 1px solid #c2cad3;
		padding-right: 18px;
		flex: 1;
	}

	.target-text {
		padding-left: 18px;
		flex: 1;
	}

	.truncate-text {
		flex: 1;
		display: -webkit-box;
		-webkit-line-clamp: 8;
		line-clamp: 8;
		-webkit-box-orient: vertical;
		overflow: hidden;
		text-overflow: ellipsis;
		position: relative;
	}

	.target-text::after,
	.source-text::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		right: 0;
		height: 1.6em;
		background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 1) 100%);
		pointer-events: none;
	}

	.langs {
		display: flex;
		width: 10%;
		border: solid #c2cad3;
		border-width: 0px 1px 1px 1px;
		border-radius: 0px 0px 10px 10px;
		align-self: center;
	}

	.source-lang {
		flex: 1;
		text-align: center;
		border-right: 1px solid #c2cad3;
	}

	.target-lang {
		flex: 1;
		text-align: center;
	}

	@media (width < 1040px) {
		.translation-container {
			width: 100%;
			flex-direction: row;
		}

		.langs {
			flex-direction: column;
			width: auto;
			border-width: 1px 1px 1px 0px;
			border-radius: 0px 10px 10px 0px;
			height: 100px;
		}

		.source-lang {
			display: flex;
			align-items: end;
			border-bottom: 1px solid #c2cad3;
			border-right: none;
		}

		.translation {
			display: flex;
			flex-direction: column;
			flex: 1;
			padding: 18px;
		}

		.source-text {
			border-right: none;
			padding-right: unset;
		}

		.target-text {
			border-top: 1px solid #c2cad3;
			padding-left: unset;
			margin-top: 18px;
			padding-top: 18px;
		}
	}

	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.6);
		backdrop-filter: blur(4px);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 1000;

		.target-text::after,
		.source-text::after {
			background: unset;
		}
	}
</style>
