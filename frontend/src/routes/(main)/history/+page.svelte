<script lang="ts">
	import History from '$lib/components/History.svelte';
	let { data } = $props();
</script>

<h1>Last translations</h1>
<History translations={data.translations} />

<style>
	h1 {
		opacity: 10%;
	}
</style>
