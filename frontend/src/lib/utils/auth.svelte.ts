import { userState } from '$lib/state/user.svelte';
import { whoami } from '$lib/sdk/sdk';
import { redirect } from '@sveltejs/kit';
import { goto } from '$app/navigation';

class AuthManager {
	channel: BroadcastChannel;
	constructor() {
		this.channel = new BroadcastChannel('auth-channel');
		this.setupListeners();
	}

	setupListeners() {
		// Listener para BroadcastChannel
		this.channel.onmessage = (event) => {
			if (event.data.type === 'LOGOUT') {
				this.remoteLogout();
			}
		};
	}

	logout = () => {
		userState.clear();
		this.channel.postMessage({ type: 'LOGOUT' });
		goto('/login');
	};

	remoteLogout = () => {
		userState.clear();
		goto('/login');
	};
}

const authManager = new AuthManager();

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
	authManager.logout();
};

export async function loginAuth() {
	if (!userState.username) {
		const res = await whoami();
		if (res) userState.set(res);
	}

	if (userState.username) {
		redirect(302, '/');
	}
}
