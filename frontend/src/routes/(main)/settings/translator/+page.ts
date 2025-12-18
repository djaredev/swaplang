import type { PageLoad } from './$types';
import { auth } from '$lib/utils/auth.svelte';
import { getAvailableLanguages, getAvailableModels, getSystemPrompt } from '$lib/sdk/sdk';

export const load: PageLoad = async () => {
	await auth();
	const availablelanguages = await getAvailableLanguages();
	const availableModels = await getAvailableModels();
	const systemPrompt = await getSystemPrompt();
	return { availablelanguages, availableModels, systemPrompt };
};
