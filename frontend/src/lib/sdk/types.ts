import type { UUID } from 'crypto';

export type UserLogin = {
	username: string;
	password: string;
};

export type UserPublic = {
	username: string;
	email: string;
};

export type Translate = {
	text: string;
	source_language: string;
	target_language: string;
};

export type Translated = {
	lang: string;
	text: string;
};

export type Translation = {
	id: UUID;
	source_lang: string;
	source_text: string;
	target_lang: string;
	target_text: string;
	created_at: string;
	updated_at: string;
};

export type GetTranslation = {
	cursor: string;
	direction?: Direction;
	limit?: number;
};

export type TranslationsPublic = {
	translations: Translation[];
	next_cursor: string | null;
};

export type Direction = 'next' | 'prev';

export type Language = {
	id: string;
	name: string;
	enabled: boolean;
};

export type LanguageUpdate = {
	id: string;
	enabled: boolean;
};

export type AvailableModels = {
	models: string[];
};

export type SystemPrompt = {
	system_prompt: string;
};

export type UpdatePassword = {
	current_password: string;
	new_password: string;
};
