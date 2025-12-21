<script lang="ts">
	import DownloadBar from './DownloadBar.svelte';

	let { isDownloading = $bindable(false) } = $props();

	let downloadEvent = $state({
		downloaded_bytes: 0,
		total_bytes: 0,
		progress_percentage: 0,
		rate: 0,
		time_remaining: 0,
		total_time: 0
	});
	let downloandState = $derived.by(() => {
		if (downloadEvent.progress_percentage >= 100) {
			return 'Downloaded model';
		}
		return 'Downloading model...';
	});
</script>

{#if isDownloading}
	<DownloadBar
		bind:state={downloandState}
		bind:downloaded={downloadEvent.downloaded_bytes}
		bind:total={downloadEvent.total_bytes}
		bind:progress={downloadEvent.progress_percentage}
		bind:rate={downloadEvent.rate}
		bind:ramainingTime={downloadEvent.time_remaining}
	/>
{/if}
