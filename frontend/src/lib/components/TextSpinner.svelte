<script lang="ts">
	let { value = $bindable('') } = $props();
</script>

<div class="loading-text">
	{value}<span class="dots"></span>
</div>

<style>
	.loading-text {
		color: #9aa0a6;
		font-size: 18px;
		font-weight: 500;
		letter-spacing: 1px;
		font-style: italic;
		animation: pulse 1.5s ease-in-out infinite;
	}

	@keyframes pulse {
		0%,
		100% {
			opacity: 1;
		}
		50% {
			opacity: 0.6;
		}
	}

	.dots {
		display: inline-block;
		width: 20px;
		text-align: left;
	}

	.dots::after {
		content: '';
		animation: dots 1.5s steps(4, end) infinite;
	}

	@keyframes dots {
		0%,
		20% {
			content: '';
		}
		40% {
			content: '.';
		}
		60% {
			content: '..';
		}
		80%,
		100% {
			content: '...';
		}
	}
</style>
