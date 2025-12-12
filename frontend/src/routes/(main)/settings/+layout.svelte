<script lang="ts">
	import { page } from '$app/state';
	import { UserCogIcon, Fingerprint, LanguagesIcon } from 'lucide-svelte';

	let { children } = $props();
</script>

<div class="content">
	<div class="settings">
		<div class="title">
			<h1>Settings</h1>
		</div>
		<div class="settings-content">
			<div class="settings-options">
				<a
					href="/settings/translator"
					class="settings-option {page.url.pathname === '/settings/translator' && 'active'}"
					title="apparance"
				>
					<LanguagesIcon class="icon" />
					<span class="option-label">Translator</span>
				</a>
				<a
					href="/settings/account"
					class="settings-option {page.url.pathname === '/settings/account' && 'active'}"
					title="account"
				>
					<UserCogIcon class="icon" />
					<span class="option-label">Account</span>
				</a>
				<a
					href="/settings/security"
					class="settings-option {page.url.pathname === '/settings/security' && 'active'}"
					title="security"
				>
					<Fingerprint class="icon" />
					<span class="option-label">Security</span>
				</a>
			</div>
			<div class="settings-view">
				{@render children()}
			</div>
		</div>
	</div>
</div>

<style>
	* {
		box-sizing: border-box;
	}

	.content {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		container: content / inline-size;
	}

	.settings {
		display: flex;
		flex-direction: column;
		max-width: 1000px;
		flex: 1;
		background: inherit;
		color: #3c4043;

		.title {
			color: inherit;
			padding: 10px 20px;

			& h1 {
				margin: 0px;
				padding: 0px;
			}
		}

		.settings-content {
			display: flex;
			gap: 50px;
			/* max-width: 1000px; */
			flex: 1;
			background: inherit;

			.settings-options {
				display: flex;
				flex-direction: column;
				gap: 4px;
				padding: 10px;
				width: 220px;
				background: inherit;

				.settings-option {
					color: inherit;
					display: flex;
					text-decoration: none;
					width: 100%;
					min-width: fit-content;
					block-size: 50px;
					align-items: center;
					gap: 20px;
					outline: 2px solid transparent;
					border-radius: 10px;
					padding: 10px;
					overflow: hidden;

					&:hover {
						background-color: #e8eaed;
					}

					.option-label {
						white-space: nowrap;
						overflow: hidden;
						transition: opacity 0.3s ease;
					}

					.icon {
						color: inherit;
					}
				}
				.active {
					/* background-color: #d7dde0; */
					background: linear-gradient(135deg, #4285f4, #34a853);
					color: white;
				}
				.disabled {
					pointer-events: none;
					opacity: 0.5;
				}
			}

			@container content ( width < 750px ) {
				.settings-options {
					flex-direction: row;
					width: 100%;
					height: 80px;
					overflow-x: scroll;
					align-items: center;
				}
			}

			.settings-view {
				display: flex;
				flex-direction: column;
				flex: 1;
				background: inherit;
				padding: 10px;
			}
		}

		@container content ( width < 750px ) {
			& {
				width: 100%;
			}

			.settings-content {
				flex-direction: column;
				width: 100%;
			}
		}
	}
</style>
