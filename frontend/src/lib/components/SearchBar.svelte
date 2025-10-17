<script lang="ts">
	import { SearchIcon, XIcon } from 'lucide-svelte';

	let value = $state();

	const clean = () => {
		value = '';
	};
</script>

<div class="search-bar">
	<SearchIcon size={20} />
	<input class="search" type="text" bind:value />
	{#if value}
		<button class="clear-btn">
			<XIcon size={20} onclick={clean} />
		</button>
	{/if}
</div>

<style>
	.search-bar {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		gap: 10px;
		width: 1000px;
		height: 48px;
		padding-right: 14px;
		padding-left: 14px;
		border: 1px solid #c2cad3;
		border-radius: 10px;
		box-shadow: 0px 0px 20px 2px rgba(0, 0, 0, 0.08);
	}

	.search {
		flex: 1;
		height: 100%;
		font-size: 18px;
		background: inherit;
		border: none;
		outline: none;
	}

	.clear-btn {
		display: flex;
		background: none;
		border: none;
		padding: 8px;
		cursor: pointer;
		border-radius: 100%;
		color: #5f6368;
	}

	.clear-btn:hover {
		background-color: #f1f3f4;
	}
</style>
