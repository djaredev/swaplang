<script lang="ts">
	import SearchBar from '$lib/components/SearchBar.svelte';
	import handler from '$lib/utils/handler';
	import type { Language } from '$lib/sdk/types';
	import { updateLanguages } from '$lib/sdk/sdk';
	import { notify } from '$lib/state/notify.svelte';
	import { SvelteMap } from 'svelte/reactivity';

	let { data } = $props();

	let langs: Language[] = $state(data.availablelanguages ? data.availablelanguages : []);

	let showSelectedOnly = $state(false);

	let query = $state('');

	let isEnabled = new SvelteMap<string, boolean>(langs.map((lang) => [lang.id, lang.enabled]));

	const toggleLangView = () => {
		showSelectedOnly = !showSelectedOnly;
		console.log(showSelectedOnly);
	};

	const clearSelection = () => {
		isEnabled.clear();
	};

	const onsubmit = handler(async () => {
		console.log('Submmitted');
		if (
			await updateLanguages(
				langs.map((lang) => ({ id: lang.id, enabled: isEnabled.get(lang.id) || false }))
			)
		) {
			snapshotEnLangs = $state.snapshot(enabledLanguages);
			notify.success('Languages updated successfully');
		} else {
			notify.error('Failed to update languages');
		}
	});

	const search = async () => {
		const q = query.toLowerCase();
		if (data.availablelanguages)
			langs = data.availablelanguages.filter((l) => l.name.toLowerCase().includes(q));
	};

	const onClean = () => {
		langs = data.availablelanguages ? data.availablelanguages : [];
	};

	const enabledLanguages = $derived(langs.filter((x) => isEnabled.get(x.id)));

	let snapshotEnLangs = $state($state.snapshot(enabledLanguages));

	$effect(() => {
		langs;
		console.log($state.snapshot(langs));
	});
</script>

<form {onsubmit} class="form">
	<div class="header">
		<h1>Available languages</h1>
		<SearchBar
			id="search"
			placeholder="Search language..."
			bind:value={query}
			oninput={search}
			{onClean}
		/>
		<button id="toggle" onclick={toggleLangView} type="button"
			>{showSelectedOnly ? 'Show all' : 'Show enabled'}</button
		>
	</div>

	<div id="grid" class="grid">
		{#each langs as lang (lang.id)}
			{#if !showSelectedOnly || isEnabled.get(lang.id)}
				<label class="lang">
					<input
						type="checkbox"
						value={lang.id}
						bind:checked={
							() => isEnabled.get(lang.id), (v) => isEnabled.set(lang.id, v ? v : false)
						}
					/>
					<div class="check">✔</div>
					<span>{lang.name}</span>
				</label>
			{/if}
		{/each}
	</div>

	<div class="footer">
		<div class="summary" id="summary">
			{enabledLanguages.length} Enabled languages
		</div>
		<div>
			<button id="clear" type="button" onclick={clearSelection}>Clear</button>
			{#if JSON.stringify(enabledLanguages) !== JSON.stringify(snapshotEnLangs)}
				<button id="save" class="primary">Save</button>
			{:else}
				<button id="save" class="primary" disabled>Save</button>
			{/if}
		</div>
	</div>
</form>

<form class="form">
	<div class="header">
		<h1>Current Model</h1>
	</div>
	<select class="select-model" disabled>
		{#if data.availableModels}
			{#each data.availableModels.models as model (model)}
				<option>{model}</option>
			{/each}
		{:else}
			<option>No models available</option>
		{/if}
	</select>
	<div class="footer">
		<div class="summary" id="summary">1 Modal available</div>
		<div>
			<button id="save" class="primary" disabled>Save</button>
		</div>
	</div>
</form>

<form class="form">
	<div class="header">
		<h1>System prompt</h1>
	</div>
	<div contenteditable="false" class="system-prompt">
		{data.systemPrompt ? data.systemPrompt.system_prompt : 'No system prompt set'}
	</div>
	<div class="footer">
		<div class="summary" id="summary">Default prompt</div>
		<div>
			<button id="reset" disabled>Reset</button>
			<button id="save" class="primary" disabled>Save</button>
		</div>
	</div>
</form>

<style>
	* {
		box-sizing: border-box;
	}

	.form {
		width: 100%;
		max-width: 900px;
		background: inherit;
		border: 1px solid #c2cad3;
		border-radius: 16px;
		padding: 1.5rem 1.75rem 1.5rem;
	}

	.header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 1.25rem;
		gap: 1rem;
		flex-wrap: wrap;
	}

	h1 {
		font-size: 1.25rem;
		font-weight: 600;
		margin: 0;
	}

	:global(.search) {
		position: relative;
		flex: 1;
		max-width: 320px;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
		gap: 0.75rem;
		margin-top: 1rem;
	}

	.lang {
		position: relative;
		border: 1px solid #c2cad3;
		border-radius: 12px;
		padding: 0.75rem 0.75rem 0.75rem 2.5rem;
		cursor: pointer;
		background: white;
		transition: all 0.2s ease;
	}

	.lang:hover {
		border-color: #4285f4;
		transform: translateY(-1px);
	}

	.lang input {
		position: absolute;
		opacity: 0;
	}

	.lang .check {
		position: absolute;
		left: 0.75rem;
		top: 50%;
		transform: translateY(-50%);
		width: 18px;
		height: 18px;
		border-radius: 5px;
		border: 1px solid #c2cad3;
		display: grid;
		place-items: center;
		color: transparent;
		transition: all 0.15s ease;
	}

	.lang input:checked + .check {
		background: linear-gradient(135deg, #4285f4, #34a853);
		border: none;
		color: white;
	}

	.footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-top: 1.5rem;
		gap: 1rem;
		flex-wrap: wrap;
	}

	.summary {
		font-size: 0.9rem;
		color: #94a3b8;
	}

	button {
		height: 40px;
		padding: 0.6rem 1rem;
		border-radius: 10px;
		border: 1px solid #c2cad3;
		background: white;
		color: inherit;
		cursor: pointer;
	}

	button.primary {
		background: linear-gradient(135deg, #4285f4, #34a853);
		border: none;
		color: #020617;
		font-weight: 600;
	}

	.select-model,
	.system-prompt {
		width: 100%;
		height: 45px;
		background: white;
		border-radius: 8px;
		border: 1px solid #c2cad3;
		outline: none;
		color: #3c4043;
		/* font-size: 16px; */
		padding: 10px;
	}

	.system-prompt {
		min-height: 150px;
		height: auto;
		max-height: 500px;
		overflow-y: auto;
		padding: 10px;
		white-space: pre-wrap;
		background: #f1f3f4;
		color: #a8a8a8;
	}

	.select-model:disabled {
		background: #f1f3f4;
		color: #a8a8a8;
		cursor: not-allowed;
	}

	button:disabled {
		opacity: 0.6;
		cursor: not-allowed;
	}
</style>
