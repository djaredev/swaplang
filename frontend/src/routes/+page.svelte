<script lang="ts">
	import LangSelect from '$lib/components/LangSelect.svelte';

	let options = [
		'Spanish',
		'English',
		'French',
		'German',
		'Italian',
		'Portuguese',
		'Russian',
		'Japanese',
		'Korean',
		'Coreano',
		'Arab',
		'Hindi'
	];

	let sourceText = $state('');
	let sourceLang = $state('Spanish');
	let targetLang = $state('English');

	const clearText = () => {
		sourceText = '';
	};

	const swapLang = () => {
		[sourceLang, targetLang] = [targetLang, sourceLang];
	};
</script>

<div class="container">
	<div class="header">
		<div class="logo">T</div>
		<h1>Traductor</h1>
	</div>

	<div class="translator-box">
		<div class="language-selector">
			<LangSelect {options} select={sourceLang} />

			<button class="swap-btn" id="swapBtn" title="Swap Languages" onclick={swapLang}>
				<svg class="swap-icon" viewBox="0 0 24 24">
					<path d="M6.99 11L3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z" />
				</svg>
			</button>

			<LangSelect {options} select={targetLang} />
		</div>

		<div class="translation-area">
			<div class="input-section">
				<div class="input-header">
					<textarea
						class="text-input"
						id="sourceText"
						placeholder="Type here to translate"
						maxlength="5000"
						bind:value={sourceText}
					></textarea>
					{#if sourceText}
						<button class="clear-btn" id="clearBtn" title="Clear text" onclick={clearText}>
							<svg viewBox="0 0 24 24">
								<path
									d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"
								/>
							</svg>
						</button>
					{/if}
				</div>
				<div class="input-content">
					<div class="char-count" id="charCount">{sourceText.length} / 5000</div>
				</div>
			</div>

			<div class="output-section">
				<div class="text-output" id="translatedText"></div>
				<div class="action-buttons">
					<button class="icon-btn" id="copyBtn" title="Copy translation">
						<svg viewBox="0 0 24 24">
							<path
								d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"
							/>
						</svg>
					</button>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.container {
		max-width: 1200px;
		margin: 0 auto;
	}

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

	h1 {
		color: #202124;
		font-size: 28px;
		font-weight: 400;
	}

	.translator-box {
		background: white;
		border-radius: 8px;
		box-shadow: 0 1px 6px rgba(32, 33, 36, 0.28);
		overflow: hidden;
	}

	.language-selector {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 18px 18px;
		border-bottom: 1px solid #e8eaed;
	}

	.swap-btn {
		background: none;
		border: none;
		cursor: pointer;
		padding: 8px;
		border-radius: 50%;
		transition: background-color 0.2s;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.swap-btn:hover {
		background-color: #f1f3f4;
	}

	.swap-icon {
		width: 24px;
		height: 24px;
		fill: #5f6368;
	}

	.translation-area {
		display: grid;
		grid-template-columns: 1fr 1fr;
		min-height: 300px;
	}

	.input-section,
	.output-section {
		display: flex;
		flex-direction: column;
	}

	.input-section {
		border-right: 1px solid #e8eaed;
	}

	.input-header {
		display: flex;
		align-items: flex-start;
		gap: 8px;
		padding: 18px 8px 0 18px;
	}

	.input-content {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 0 18px 18px 18px;
	}

	.output-section {
		padding: 18px;
		display: flex;
		flex-direction: column;
	}

	.text-input {
		width: 100%;
		border: none;
		outline: none;
		font-size: 18px;
		font-family: inherit;
		resize: none;
		min-height: 200px;
		color: #3c4043;
	}

	.text-input::placeholder {
		color: #9aa0a6;
	}

	.text-output {
		width: 100%;
		font-size: 18px;
		color: #3c4043;
		min-height: 200px;
		line-height: 1.5;
	}

	.char-count {
		color: #5f6368;
		font-size: 12px;
		margin-top: auto;
		padding-top: 12px;
	}

	.clear-btn {
		background: none;
		border: none;
		cursor: pointer;
		padding: 8px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #5f6368;
		flex-shrink: 0;
		transform: translate(0px, -8px);
	}

	.clear-btn:hover {
		background-color: #f1f3f4;
	}

	.clear-btn svg {
		width: 20px;
		height: 20px;
		fill: currentColor;
	}

	.action-buttons {
		display: flex;
		gap: 8px;
		margin-top: auto;
		padding-top: 12px;
	}

	.icon-btn {
		background: none;
		border: none;
		cursor: pointer;
		padding: 8px;
		border-radius: 50%;
		transition: background-color 0.2s;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #5f6368;
	}

	.icon-btn:hover {
		background-color: #f1f3f4;
	}

	.icon-btn:active {
		background-color: #e8eaed;
	}

	.icon-btn svg {
		width: 20px;
		height: 20px;
		fill: currentColor;
	}

	@media (max-width: 768px) {
		.translation-area {
			grid-template-columns: 1fr;
		}

		.input-section {
			border-right: none;
			border-bottom: 1px solid #e8eaed;
		}

		h1 {
			font-size: 22px;
		}
	}

	.loading {
		color: #9aa0a6;
		font-style: italic;
	}
</style>
