<script lang="ts">
	import { page } from '$app/state';
	import { CircleXIcon } from 'lucide-svelte';
</script>

<div class="container">
	<div class="error">
		<CircleXIcon size={50} />
		<h1>{page.status}: {page.error?.message}</h1>
	</div>
</div>

<style>
	* {
		box-sizing: border-box;
	}

	.container {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		color: #d20f39;
		padding: 20px;
	}
	.error {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 20px;
		width: 600px;
		padding: 20px;
		background: white;
		border: 1px solid #c2cad3;
		border-radius: 10px;
		overflow: hidden;
		@media (width <= 600px) {
			& {
				flex-direction: column;
				width: 100%;
				height: auto;
			}
		}
	}
</style>
