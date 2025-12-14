<script lang="ts">
	import SearchBar from '$lib/components/SearchBar.svelte';
	import handler from '$lib/utils/handler';

	let langs = $state([
		{ id: 'es', name: 'Spanish', enabled: true },
		{ id: 'en', name: 'English', enabled: true },
		{ id: 'fr', name: 'French', enabled: false },
		{ id: 'de', name: 'German', enabled: false },
		{ id: 'it', name: 'Italian', enabled: false },
		{ id: 'pt', name: 'Portuguese', enabled: false },
		{ id: 'ru', name: 'Russian', enabled: false },
		{ id: 'ja', name: 'Japanese', enabled: false },
		{ id: 'ko', name: 'Korean', enabled: false },
		{ id: 'ar', name: 'Arabic', enabled: false },
		{ id: 'hi', name: 'Hindi', enabled: false }
	]);

	let showSelectedOnly = $state(false);

	const toggleLangView = () => {
		showSelectedOnly = !showSelectedOnly;
		console.log(showSelectedOnly);
	};

	const clearSelection = () => {
		langs = langs.map((lang) => ({ ...lang, enabled: false }));
	};

	const onsubmit = handler(async () => {});
	$effect(() => {
		langs;
		console.log($state.snapshot(langs));
	});
</script>

<form {onsubmit} class="lang-select">
	<div class="header">
		<h1>Available languages</h1>
		<SearchBar id="search" placeholder="Search language..." />
		<button id="toggle" onclick={toggleLangView}
			>{showSelectedOnly ? 'Show all' : 'Show enabled'}</button
		>
	</div>

	<div id="grid" class="grid">
		{#each langs as lang (lang.id)}
			{#if !showSelectedOnly || lang.enabled}
				<label class="lang">
					<input type="checkbox" value={lang.id} bind:checked={lang.enabled} />
					<div class="check">✔</div>
					<span>{lang.name}</span>
				</label>
			{/if}
		{/each}
	</div>

	<div class="footer">
		<div class="summary" id="summary">
			{langs.filter((x) => x.enabled).length} Enabled languages
		</div>
		<div>
			<button id="clear" onclick={clearSelection}>Clear</button>
			<button id="save" class="primary">Save</button>
		</div>
	</div>
</form>

<style>
	.profile {
		display: flex;
		flex-direction: column;
		gap: 10px;
		border: 1px solid #e8eaed;
		border-radius: 8px;
		padding: 20px;
		/* background: white; */

		.label {
			color: inherit;
			text-align: left;
			padding: 2px;
		}

		:global(.button) {
			align-self: end;
		}
	}

	:root {
		--bg: #0f172a;
		--panel: #020617;
		--border: #1e293b;
		--primary: #38bdf8;
		--primary-soft: #0ea5e9;
		--text: #e5e7eb;
		--muted: #94a3b8;
	}

	* {
		box-sizing: border-box;
	}

	.lang-select {
		width: 100%;
		max-width: 900px;
		background: inherit;
		border: 1px solid #c2cad3;
		border-radius: 16px;
		padding: 1.5rem 1.75rem 2rem;
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
		color: var(--muted);
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
</style>
