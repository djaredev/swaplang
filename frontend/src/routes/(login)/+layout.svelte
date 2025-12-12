<script>
	import '../../app.css';

	let { children } = $props();
</script>

{@render children()}

<style>
	:global(html) {
		height: 100%;
		width: 100%;
	}

	:global(body) {
		display: flex;
		height: 100%;
		width: 100%;
		margin: 0;
		padding: 0;
		/* background: #11111b; */
		box-sizing: border-box;
	}
</style>
