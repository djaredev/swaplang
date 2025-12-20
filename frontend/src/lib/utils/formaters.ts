export function bytesToFormattedSize(bytes: number): string {
	const MB = 1_000_000;
	const GB = 1_000_000_000;

	if (bytes >= GB) {
		return `${(bytes / GB).toFixed(2)} GB`;
	}

	return `${(bytes / MB).toFixed(2)} MB`;
}

export function secondsToTimeFormat(totalSeconds: number): string {
	const hours = Math.floor(totalSeconds / 3600);
	const minutes = Math.floor((totalSeconds % 3600) / 60);
	const seconds = totalSeconds % 60;

	if (hours > 0) {
		return `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
	}

	return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}
