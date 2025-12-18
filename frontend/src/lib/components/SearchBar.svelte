<script lang="ts">
	import { SearchIcon, XIcon } from 'lucide-svelte';

	let { value = $bindable(), onClean, ...restProps } = $props();

	const clean = () => {
		value = '';
		onClean?.();
	};
</script>

<div class="search-bar">
	<div class="icon-bar">
		<SearchIcon size={20} />
	</div>
	<input class="search" type="text" bind:value {...restProps} />
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
		width: 300px;
		height: 40px;
		background: white;
		padding-right: 14px;
		padding-left: 14px;
		border: 1px solid #c2cad3;
		border-radius: 10px;
		overflow: hidden;
	}

	.icon-bar {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		max-width: 20px;
		flex: 1;
	}

	.search {
		width: 100%;
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
