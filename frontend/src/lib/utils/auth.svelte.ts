import { userState } from '$lib/state/user.svelte';
import { whoami } from '$lib/sdk/sdk';
import { redirect } from '@sveltejs/kit';
import { goto } from '$app/navigation';

export async function auth() {
	if (!userState.username) {
		const res = await whoami();
		if (res) userState.set(res);
	}

	if (!userState.username) {
		redirect(302, '/login');
	}
}

export const logout = () => {
	userState.clear();
	goto('/login');
};
