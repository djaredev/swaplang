import type {
	AvailableModels,
	GetTranslation,
	Language,
	LanguageUpdate,
	SystemPrompt,
	Translate,
	Translated,
	TranslationsPublic,
	UpdatePassword,
	UpdateUser,
	UserLogin,
	UserPublic,
	UserUpdate
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

export const getAvailableLanguages = async (
	onlyEnabled: boolean = false
): Promise<Language[] | null> => {
	const response = await fetch(
		apiUrl('/settings/languages', { only_enabled: onlyEnabled.toString() }),
		{
			credentials: 'include'
		}
	);

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

export const getAvailableModels = async (): Promise<AvailableModels | null> => {
	const response = await fetch(apiUrl('/settings/models'), {
		credentials: 'include'
	});
	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}
	return await response.json();
};

export const getSystemPrompt = async (): Promise<SystemPrompt | null> => {
	const response = await fetch(apiUrl('/settings/system_prompt'), {
		credentials: 'include'
	});
	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}
	return await response.json();
};

export const updatePasswordMe = async (updatePassword: UpdatePassword): Promise<boolean> => {
	console.log(JSON.stringify(updatePassword));
	const response = await fetch(apiUrl('/users/me/password'), {
		method: 'PATCH',
		headers: { 'content-type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(updatePassword)
	});
	console.log('fetch');
	if (!response.ok) {
		notify.error((await response.json()).detail);
		console.log('Error');
		return false;
	}
	return true;
};

export const updateUserMe = async (updateUser: UserUpdate): Promise<UserPublic | null> => {
	const response = await fetch(apiUrl('/users/me'), {
		method: 'PATCH',
		headers: { 'content-type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(updateUser)
	});
	if (!response.ok) {
		notify.error((await response.json()).detail);
		return null;
	}
	return await response.json();
};
