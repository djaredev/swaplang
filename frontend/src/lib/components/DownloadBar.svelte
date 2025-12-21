<script lang="ts">
	import { ArrowDownUpIcon, DownloadIcon, EllipsisVerticalIcon, TimerIcon } from 'lucide-svelte';
	import ProgressBar from './ProgressBar.svelte';
	import { bytesToFormattedSize, secondsToTimeFormat } from '$lib/utils/formaters';

	let {
		ramainingTime = $bindable(0),
		progress = $bindable(0),
		downloaded = $bindable(0),
		total = $bindable(0),
		rate = $bindable(0),
		state = $bindable('')
	} = $props();
</script>

<div class="download-bar">
	<div class="top-stats">
		<span class="stat">
			<div class="label">{state}</div>
		</span>
		<span class="stat percentage">{progress < 100 ? `${Math.floor(progress)}%` : 'Completed!'}</span
		>
	</div>

	<ProgressBar bind:progress />

	<div class="bottom-stats">
		<div class="stat" style="flex-grow: 1; display: flex; justify-content: start;">
			<div class="icon">
				<TimerIcon size="14" />
			</div>
			<div class="label">
				{secondsToTimeFormat(Math.floor(ramainingTime))}
			</div>
		</div>
		<span class="stat">
			<div class="icon">
				<DownloadIcon size="14" />
			</div>
			<div class="label">
				{`${bytesToFormattedSize(Math.floor(downloaded))} / ${bytesToFormattedSize(Math.floor(total))}`}
			</div>
		</span>
		<span class="split">
			<div class="icon">
				<EllipsisVerticalIcon size="14" />
			</div>
		</span>
		<span class="stat">
			<div class="icon">
				<ArrowDownUpIcon size="14" />
			</div>
			<div class="label">
				{bytesToFormattedSize(Math.ceil(rate))}/s
			</div>
		</span>
	</div>
</div>

<style>
	.top-stats {
		display: flex;
		justify-content: space-between;
		margin-bottom: 8px;
		font-size: 14px;
		color: #5f6368;
	}

	.bottom-stats {
		display: flex;
		justify-content: end;
		font-size: 14px;
		color: #5f6368;
		gap: 10px;
	}

	.stat,
	.icon,
	.split {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.stat {
		gap: 4px;
	}

	.label {
		height: 12px;
	}

	.percentage {
		font-weight: bold;
		font-size: 16px;
		color: #34a853;
	}
</style>
