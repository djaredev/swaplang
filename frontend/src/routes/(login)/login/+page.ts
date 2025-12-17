import type { PageLoad } from './$types';
import { loginAuth } from '$lib/utils/auth.svelte';

export const load: PageLoad = async () => {
	await loginAuth();
};
