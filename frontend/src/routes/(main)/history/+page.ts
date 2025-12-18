import type { PageLoad } from './$types';
import { auth } from '$lib/utils/auth.svelte';
import { getTranslations } from '$lib/sdk/sdk';

export const load: PageLoad = async () => {
	await auth();
	const translations = await getTranslations({ limit: 10 });
	return { translations };
};
