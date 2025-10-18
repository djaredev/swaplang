const API_URL = import.meta.env.VITE_API_URL;

export const apiUrl = (route: string): string => {
	return `${API_URL}/api${route}`;
};
