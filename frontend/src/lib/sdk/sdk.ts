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
	UserLogin,
	UserPublic,
	UserUpdate
} from './types';
import { apiUrl } from './utils';
import { handleError } from './interceptors';

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
		handleError(response);
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
		handleError(response);
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
		handleError(response);
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
		handleError(response);
		return false;
	}

	return true;
};

export const getAvailableModels = async (): Promise<AvailableModels | null> => {
	const response = await fetch(apiUrl('/settings/models'), {
		credentials: 'include'
	});
	if (!response.ok) {
		handleError(response);
		return null;
	}
	return await response.json();
};

export const getSystemPrompt = async (): Promise<SystemPrompt | null> => {
	const response = await fetch(apiUrl('/settings/system_prompt'), {
		credentials: 'include'
	});
	if (!response.ok) {
		handleError(response);
		return null;
	}
	return await response.json();
};

export const updatePasswordMe = async (updatePassword: UpdatePassword): Promise<boolean> => {
	const response = await fetch(apiUrl('/users/me/password'), {
		method: 'PATCH',
		headers: { 'content-type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(updatePassword)
	});
	if (!response.ok) {
		handleError(response);
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
		handleError(response);
		return null;
	}
	return await response.json();
};

export const eventSource = new EventSource(apiUrl('/sse'));
