<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import Field from '$lib/components/Field.svelte';
	import { userState } from '$lib/state/user.svelte';
	import { notify } from '$lib/state/notify.svelte';
	import handler from '$lib/utils/handler';
	import { updateUserMe } from '$lib/sdk/sdk';
	import type { UserUpdate } from '$lib/sdk/types';

	const account: UserUpdate = $state({
		username: userState.username,
		email: userState.email
	});

	const onsubmit = handler(async () => {
		const res = await updateUserMe({
			username: account.username !== userState.username ? account.username : undefined,
			email: account.email !== userState.email ? account.email : undefined
		});
		if (res) {
			if (res.username !== userState.username) {
				notify.success('Updated username');
			}
			if (res.email !== userState.email) {
				notify.success('Updated email');
			}
			userState.set(res);
		}
	});
</script>

<form {onsubmit} class="profile">
	<label for="username" class="label">Username</label>
	<Field id="username" type="text" bind:value={account.username} />
	<label for="email" class="label">Email</label>
	<Field id="email" type="email" bind:value={account.email} />
	{#if account.username === userState.username && account.email === userState.email}
		<Button type="submit" disabled>Save</Button>
	{:else}
		<Button type="submit">Save</Button>
	{/if}
</form>

<style>
	.profile {
		display: flex;
		flex-direction: column;
		gap: 10px;
		border: 1px solid #c2cad3;
		border-radius: 16px;
		padding: 20px;

		.label {
			color: #3c4043;
			text-align: left;
			padding: 2px;
		}

		:global(.button) {
			align-self: end;
			color: white;
		}
	}
</style>
