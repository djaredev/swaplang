<script lang="ts">
	let { progress = $bindable(0) } = $props();
</script>

<div class="progress-bar">
	<div class="progress-fill" style:width={`${progress}%`}></div>
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
		height: 100%;
		background: linear-gradient(135deg, #4285f4, #34a853);
		border-radius: 15px;
		transition: width 0.3s ease;
		position: relative;
		overflow: hidden;
	}
</style>
