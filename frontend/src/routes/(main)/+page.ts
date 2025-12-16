import type { PageLoad } from './$types';
import { auth } from '$lib/utils/auth.svelte';
import { getAvailableLanguages } from '$lib/sdk/sdk';

export const load: PageLoad = async () => {
	await auth();
	const langs = await getAvailableLanguages(true);
	return { langs };
};
