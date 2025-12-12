import { type UserPublic } from '$lib/sdk/types';

class UserState {
	username: string = $state('');
	email: string = $state('');

	set = (user: UserPublic) => {
		this.username = user.username;
		this.email = user.email;
	};

	get = () => {
		return {
			username: this.username,
			email: this.email
		};
	};

	clear = () => {
		this.username = '';
		this.email = '';
	};
}

export const userState = new UserState();
