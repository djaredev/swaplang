import { userState } from '$lib/state/user.svelte';
import { whoami } from '$lib/sdk/sdk';
import { redirect } from '@sveltejs/kit';

export async function auth() {
	if (!userState.username) {
		const res = await whoami();
		if (res) userState.set(res);
	}

	if (!userState.username) {
		redirect(302, '/login');
	}
}
