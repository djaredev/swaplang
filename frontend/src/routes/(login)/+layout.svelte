<script>
	import '../../app.css';

	let { children } = $props();
</script>

<svelte:body />

<main class="body">
	{@render children()}
</main>

<style>
	:global(html) {
		height: 100%;
		width: 100%;
	}

	.body {
		display: flex;
		height: 100%;
		width: 100%;
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}
</style>
