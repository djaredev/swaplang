import type { UserLogin, UserPublic } from './types';
import type { Translate, Translated, UserLogin, UserPublic } from './types';
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
