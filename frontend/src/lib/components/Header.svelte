<script>
	import AppOptions from './AppOptions.svelte';
</script>

<header class="header">
	<a class="swaplang" href="/">
		<div class="logo">
			<div class="icon">S</div>
		</div>
		<div class="title">
			<div>Swaplang</div>
		</div>
	</a>
	<div class="menu">
		<AppOptions />
	</div>
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

	.icon {
		user-select: none;
		height: 18px;
	}

	.swaplang {
		display: flex;
		align-items: center;
		gap: 10px;
		text-decoration: none;
		color: inherit;
	}

	.title {
		height: 40px;
		flex: 1;
		display: flex;
		align-items: center;
		color: black;
		font-weight: bold;
		font-size: 20px;

		& div {
			height: 18px;
		}
	}

	.menu {
		display: flex;
		flex: 1;
		align-items: end;
		justify-content: end;
	}
</style>
