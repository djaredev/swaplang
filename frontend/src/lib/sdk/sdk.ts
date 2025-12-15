import type {
	GetTranslation,
	Language,
	LanguageUpdate,
	Translate,
	Translated,
	TranslationsPublic,
	UserLogin,
	UserPublic
} from './types';
import { apiUrl } from './utils';
import { notify } from '$lib/state/notify.svelte';

export const login = async (userLogin: UserLogin): Promise<Response> => {
	const response = await fetch(apiUrl('/login'), {
		method: 'POST',
		headers: { 'content-type': 'application/x-www-form-urlencoded' },
		credentials: 'include',
		body: new URLSearchParams(userLogin).toString()
	});

	return response;
};

export const logout = async (): Promise<Response> => {
	const response = await fetch(apiUrl('/logout'), {
		method: 'POST',
		credentials: 'include'
	});
	return response;
};

export const whoami = async (): Promise<UserPublic | null> => {
	const response = await fetch(apiUrl('/whoami'), {
		credentials: 'include'
	});
	if (!response.ok) {
		return null;
	}
	return await response.json();
};

export const translate = async (data: Translate): Promise<Translated | null> => {
	const response = await fetch(apiUrl('/translate', data), {
		method: 'POST',
		credentials: 'include'
	});

	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}

	return await response.json();
};

export const getTranslations = async (
	data?: GetTranslation
): Promise<TranslationsPublic | null> => {
	const response = await fetch(apiUrl('/translation', data), {
		credentials: 'include'
	});

	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}

	return await response.json();
};

export const getAvailableLanguages = async (): Promise<Language[] | null> => {
	const response = await fetch(apiUrl('/settings/languages'), {
		credentials: 'include'
	});

	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}

	return await response.json();
};

export const updateLanguages = async (languages: LanguageUpdate[]): Promise<boolean> => {
	const response = await fetch(apiUrl('/settings/languages'), {
		method: 'PUT',
		headers: { 'content-type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(languages)
	});

	if (!response.ok) {
		notify.error((await response.json()).detail);
		return false;
	}

	return true;
};
