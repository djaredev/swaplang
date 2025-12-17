import { notify } from '$lib/state/notify.svelte';
import { logout } from '$lib/utils/auth.svelte';

export const handleError = async (response: Response) => {
	if (response.status === 401 || response.status === 403) {
		logout();
		return;
	}
	notify.error((await response.json()).detail);
};
