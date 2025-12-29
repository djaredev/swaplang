<script lang="ts">
	import { ArrowDownUpIcon, DownloadIcon, EllipsisVerticalIcon, TimerIcon } from 'lucide-svelte';
	import ProgressBar from './ProgressBar.svelte';
	import { bytesToFormattedSize, secondsToTimeFormat } from '$lib/utils/formaters';

	export type Barstyle = 'bar-downloading' | 'bar-error';

	type Props = {
		ramainingTime: number;
		progress: number;
		downloaded: number;
		total: number;
		rate: number;
		state: string;
		barStyle: Barstyle;
	};

	let {
		ramainingTime = $bindable(0),
		progress = $bindable(0),
		downloaded = $bindable(0),
		total = $bindable(0),
		rate = $bindable(0),
		state = $bindable(''),
		barStyle = 'bar-downloading'
	}: Props = $props();
</script>

<div class="download-bar">
	<div class="top-stats">
		<span class="stat">
			<div class={['label', barStyle]}>{state}</div>
		</span>
		<span class={['stat percentage', barStyle]}
			>{progress < 100 ? `${Math.floor(progress)}%` : 'Completed!'}</span
		>
	</div>

	<ProgressBar bind:progress color={barStyle} />

	<div class="bottom-stats">
		<div class="stat" style="flex-grow: 1; display: flex; justify-content: start;">
			<div class="icon">
				<TimerIcon size="14" />
			</div>
			<div class="label">
				{barStyle == 'bar-downloading' ? secondsToTimeFormat(Math.floor(ramainingTime)) : '--:--'}
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
				{barStyle == 'bar-downloading' ? bytesToFormattedSize(Math.ceil(rate)) : '0 MB/s'}/s
			</div>
		</span>
	</div>
</div>

<style>
	:global(.bar-error) {
		color: #d41313;
		background: linear-gradient(135deg, #c98510, #d41313);
	}

	:global(.bar-downloading) {
		color: #34a853;
		background: linear-gradient(135deg, #4285f4, #34a853);
	}

	.top-stats .bar-error,
	.top-stats .bar-downloading {
		background: inherit;
	}

	.label.bar-downloading {
		color: #5f6368;
	}

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
	}
</style>
