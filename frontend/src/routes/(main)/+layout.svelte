<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Notify from '$lib/components/Notify.svelte';

	let { children } = $props();
</script>

<Header />
<Notify />
<main>
	{@render children?.()}
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		flex: 1;
	}
</style>
