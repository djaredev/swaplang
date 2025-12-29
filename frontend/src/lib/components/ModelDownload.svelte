<script lang="ts">
	import { eventSource } from '$lib/sdk/sdk';
	import { tick } from 'svelte';
	import DownloadBar, { type Barstyle } from './DownloadBar.svelte';

	let { isDownloading = $bindable(false) } = $props();

	let downloadStart = $state({
		downloaded_bytes: 0,
		total_bytes: 0,
		progress_percentage: 0,
		rate: 0,
		time_remaining: 0,
		total_time: 0
	});

	let downloadEvent = $state(downloadStart);

	let downloadState = $state('');

	let barStyle: Barstyle = $state('bar-downloading');

	eventSource.addEventListener('model_download_started', () => {
		downloadState = 'Starting model download...';
		barStyle = 'bar-downloading';
		isDownloading = true;
		downloadEvent = downloadStart;
	});

	eventSource.addEventListener('model_download_progress', (event) => {
		downloadEvent = JSON.parse(event.data);
		downloadState = 'Downloading model...';
	});

	eventSource.addEventListener('model_download_completed', () => {
		downloadState = 'Model downloaded';
		tick().then(() => {
			setTimeout(() => (isDownloading = false), 500);
		});
	});

	eventSource.addEventListener('model_download_failed', () => {
		downloadState = 'Model download failed';
		barStyle = 'bar-error';
	});
</script>

{#if isDownloading}
	<DownloadBar
		bind:state={downloadState}
		bind:downloaded={downloadEvent.downloaded_bytes}
		bind:total={downloadEvent.total_bytes}
		bind:progress={downloadEvent.progress_percentage}
		bind:rate={downloadEvent.rate}
		bind:ramainingTime={downloadEvent.time_remaining}
		{barStyle}
	/>
{/if}
