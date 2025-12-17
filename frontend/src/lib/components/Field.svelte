<script lang="ts">
	let { class: className = '', value = $bindable(), ...restProps } = $props();
</script>

<input class={['field', className]} bind:value {...restProps} />

<style>
	* {
		box-sizing: border-box;
	}
	.field {
		width: 100%;
		height: 45px;
		background: white;
		color: #cdd6f4;
		border-radius: 8px;
		border: 1px solid #c2cad3;
		outline: none;
		color: #3c4043;
		font-size: 16px;
		padding: 10px;
	}

	.field:focus {
		border-color: #8ab4f8;
		box-shadow: 0 0 0 4px #d2e3fc;
	}
</style>
