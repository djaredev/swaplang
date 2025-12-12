<script>
	import AppOptions from './AppOptions.svelte';
</script>

<header class="header">
	<div class="logo">T</div>
	<h1 class="title">Traductor</h1>
	<AppOptions />
</header>

<style>
	.header {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 30px;
		padding: 20px 0;
	}

	.logo {
		width: 40px;
		height: 40px;
		background: linear-gradient(135deg, #4285f4, #34a853);
		border-radius: 8px;
		display: flex;
		align-items: center;
		justify-content: center;
		color: white;
		font-weight: bold;
		font-size: 20px;
	}

	.title {
		flex: 1;
	}
</style>
