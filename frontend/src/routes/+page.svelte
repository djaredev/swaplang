<script lang="ts">
	import AppOptions from '$lib/components/AppOptions.svelte';
	import LangSelect from '$lib/components/LangSelect.svelte';
	import { HistoryIcon } from 'lucide-svelte';
	import { translate } from '$lib/sdk/sdk';

	let langs = [
		{ id: 'es', name: 'Spanish' },
		{ id: 'en', name: 'English' },
		{ id: 'fr', name: 'French' },
		{ id: 'de', name: 'German' },
		{ id: 'it', name: 'Italian' },
		{ id: 'pt', name: 'Portuguese' },
		{ id: 'ru', name: 'Russian' },
		{ id: 'ja', name: 'Japanese' },
		{ id: 'ko', name: 'Korean' },
		{ id: 'ar', name: 'Arabic' },
		{ id: 'hi', name: 'Hindi' }
	];

	let typingTime: NodeJS.Timeout;
	let input: HTMLDivElement;

	let sourceText = $state('');
	let targetText = $state('');
	let sourceLang = $state('es');
	let targetLang = $state('en');

	const clearText = () => {
		sourceText = '';
		targetText = '';
		clearTimeout(typingTime);
	};

	const swapLang = () => {
		[sourceLang, targetLang] = [targetLang, sourceLang];
		sourceText = targetText;
		targetText = '';
		getTranslation();
	};

	const getTranslation = async () => {
		if (sourceLang === targetLang || sourceText === '') {
			clearTimeout(typingTime);
			return;
		}
		clearTimeout(typingTime);
		typingTime = setTimeout(async () => {
			const data = await translate({
				text: sourceText,
				source_language: sourceLang,
				target_language: targetLang
			});
			console.log(data);
			targetText = data.text;
		}, 3000);
	};

	const copyToClipboard = async () => {
		await navigator.clipboard.writeText(targetText);
	};

	const fixtInput = () => {
		if (sourceText === '\n') {
			sourceText = '';
			clearText();
		}
	};

	const maxlength = (e: InputEvent) => {
		const text = input.innerText;

		// Always allow deletion
		if (e.inputType.includes('delete')) {
			return;
		}

		// Cancel if the limit has already been reached
		if (text.length >= 5000) {
			e.preventDefault();
		}
	};
</script>

<div class="content">
	<div class="translator-box">
		<div class="language-selector">
			<LangSelect options={langs} bind:value={sourceLang} />

			<button class="swap-btn" id="swapBtn" title="Swap Languages" onclick={swapLang}>
				<svg class="swap-icon" viewBox="0 0 24 24">
					<path d="M6.99 11L3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z" />
				</svg>
			</button>

			<LangSelect options={langs} bind:value={targetLang} onchange={getTranslation} />
		</div>

		<div class="translation-area">
			<div class="input-section">
				<div class="input-header">
					<div
						class="text-input"
						id="translatedText"
						placeholder="Type here to translate"
						contenteditable="plaintext-only"
						bind:innerText={sourceText}
						bind:this={input}
						oninput={() => {
							fixtInput();
							getTranslation();
						}}
						onbeforeinput={maxlength}
					></div>
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
				<div
					class="text-output"
					id="translatedText"
					contenteditable="plaintext-only"
					bind:innerText={targetText}
				></div>
				<div class="action-buttons">
					{#if targetText}
						<button
							class="icon-btn"
							id="copyBtn"
							title="Copy translation"
							onclick={copyToClipboard}
						>
							<svg viewBox="0 0 24 24">
								<path
									d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"
								/>
							</svg>
						</button>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>
<div class="footer">
	<a
		class="history-btn"
		href="/history"
		title="Translation History"
		data-sveltekit-preload-data="off"
	>
		<HistoryIcon size="40" color="#5f6368" />
	</a>
	<div>History</div>
</div>

<style>
	.footer {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		bottom: 20px;
		right: 20px;
		padding: 40px;
		gap: 10px;
	}
	.history-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 70px;
		height: 70px;
		background: white;
		border-radius: 50%;
		box-shadow: 0 1px 6px rgba(32, 33, 36, 0.28);
		border: none;
	}

	.history-btn:hover {
		background-color: #f1f3f4;
	}
	.container {
		/* max-width: 1200px; */
		margin: 0 auto;
	}

	.content {
		display: flex;
		/* flex-direction: column; */
		align-items: center;
		justify-content: center;
		/* width: 100%; */
		/* padding: 20px; */
	}

	.title {
		flex: 1;
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
		/* flex: 1; */
		width: 1200px;
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
		overflow: hidden;
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

	.text-input:empty::before {
		content: attr(placeholder);
		color: #9aa0a6;
	}

	.text-input,
	.text-output {
		width: 100%;
		font-size: 18px;
		color: #3c4043;
		min-height: 200px;
		line-height: 1.2;
		outline: none;
		overflow-y: auto;
		white-space: pre-wrap;
		word-wrap: break-word;
		overflow-wrap: break-word;
	}

	.text-output {
		pointer-events: none;
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
