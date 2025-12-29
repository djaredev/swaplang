import { notify } from '$lib/state/notify.svelte';
import { logout } from '$lib/utils/auth.svelte';

export const handleError = async (response: Response) => {
	console.log(response);
	if (response.status === 401 || response.status === 403) {
		logout();
		return;
	}
	if (response.status === 500) {
		notify.error('A server error occurred. Please try again.');
	}
	notify.error((await response.json()).detail);
};
