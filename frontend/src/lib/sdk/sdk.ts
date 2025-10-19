import type { UUID } from 'crypto';
import type {
	GetTranslation,
	Id,
	Translate,
	Translated,
	TranslationsPublic,
	UserLogin,
	UserPublic
} from './types';
import { apiUrl } from './utils';

export const login = async (userLogin: UserLogin): Promise<UserPublic> => {
	const response = await fetch(apiUrl('/login'), {
		method: 'POST',
		headers: { 'content-type': 'application/x-www-form-urlencoded' },
		credentials: 'include',
		body: new URLSearchParams(userLogin).toString()
	});

	if (!response.ok) {
		throw new Error(`Error: ${response.status}`);
	}

	return await response.json();
};

export const translate = async (data: Translate): Promise<Translated> => {
	const response = await fetch(apiUrl('/translate', data), {
		method: 'POST',
		credentials: 'include'
	});

	if (!response.ok) {
		throw new Error(`Error: ${response.status}`);
	}

	return await response.json();
};

export const getTranslations = async (data?: GetTranslation): Promise<TranslationsPublic> => {
	const response = await fetch(apiUrl('/translation', data), {
		credentials: 'include'
	});

	if (!response.ok) {
		throw new Error(`Response Error: ${response.status}`);
	}

	return await response.json();
};

export const deleteTranslation = async (id: UUID) => {
	const response = await fetch(apiUrl(`/translation/${id}`), {
		method: 'DELETE',
		credentials: 'include'
	});

	if (!response.ok) {
		throw new Error(`Response Error: ${response.status}`);
	}
};
