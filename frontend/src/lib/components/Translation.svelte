<script lang="ts">
	let { translation } = $props();
</script>

<div class="translation-container">
	<div class="langs">
		<div class="source-lang">{translation.sourceLang}</div>
		<div class="target-lang">{translation.targetLang}</div>
	</div>
	<div class="translation">
		<div class="source-text">
			{translation.sourceText}
		</div>
		<div class="target-text">
			{translation.targetText}
		</div>
	</div>
</div>

<style>
	* {
		box-sizing: border-box;
	}

	.translation-container {
		display: flex;
		flex-direction: column;
		width: 1000px;
		border: 1px solid #c2cad3;
		border-radius: 10px;
		box-shadow: 0px 0px 20px 2px rgba(0, 0, 0, 0.08);
		overflow: hidden;
	}

	.translation {
		display: flex;
		flex: 1;
		padding: 18px;
	}

	.source-text {
		border-right: 1px solid #c2cad3;
		padding-right: 18px;
	}

	.target-text {
		padding-left: 18px;
	}

	.source-text,
	.target-text {
		flex: 1;
		display: -webkit-box;
		-webkit-line-clamp: 8;
		line-clamp: 8;
		-webkit-box-orient: vertical;
		overflow: hidden;
		text-overflow: ellipsis;
		position: relative;
	}

	.target-text::after,
	.source-text::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		right: 0;
		height: 1.6em;
		background: linear-gradient(to bottom, rgba(248, 249, 250, 0) 0%, rgba(248, 249, 250, 1) 100%);
		pointer-events: none;
	}

	.langs {
		display: flex;
		width: 10%;
		border: solid #c2cad3;
		border-width: 0px 1px 1px 1px;
		border-radius: 0px 0px 10px 10px;
		align-self: center;
	}

	.source-lang {
		flex: 1;
		text-align: center;
		border-right: 1px solid #c2cad3;
	}

	.target-lang {
		flex: 1;
		text-align: center;
	}

	@media (width < 1000px) {
		.translation-container {
			width: 100%;
			flex-direction: row;
		}

		.langs {
			flex-direction: column;
			width: auto;
			border-width: 1px 1px 1px 0px;
			border-radius: 0px 10px 10px 0px;
			height: 100px;
		}

		.source-lang {
			display: flex;
			align-items: end;
			border-bottom: 1px solid #c2cad3;
			border-right: none;
		}

		.translation {
			display: flex;
			flex-direction: column;
			flex: 1;
			padding: 18px;
		}

		.source-text {
			border-right: none;
			padding-right: unset;
		}

		.target-text {
			border-top: 1px solid #c2cad3;
			padding-left: unset;
			margin-top: 18px;
			padding-top: 18px;
		}
	}
</style>
