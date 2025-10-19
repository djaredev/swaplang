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
