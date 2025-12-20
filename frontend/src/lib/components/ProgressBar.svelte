<script lang="ts">
	import { Tween } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';

	let { progress = $bindable(0) } = $props();

	const tween = Tween.of(() => progress, {
		duration: 400,
		easing: cubicOut
	});
</script>

<div class="progress-bar">
	<div class="progress-fill" style:transform={`translateX(${-100 + tween.current}%)`}></div>
</div>

<style>
	.progress-bar {
		width: 100%;
		height: 12px;
		background: #e0e0e0;
		border-radius: 15px;
		overflow: hidden;
		position: relative;
		margin-bottom: 20px;
		box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.progress-fill {
		width: 100%;
		height: 100%;
		background: linear-gradient(135deg, #4285f4, #34a853);
		border-radius: 15px;
		position: relative;
		overflow: hidden;
	}
</style>
