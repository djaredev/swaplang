const API_URL = import.meta.env.VITE_API_URL || '';

export const apiUrl = (
	route: string,
	params?: string | string[][] | Record<string, string>
): string => {
	let url = `${API_URL}/api${route}`;
	if (params) {
		url += `?${new URLSearchParams(params)}`;
	}
	return url;
};
