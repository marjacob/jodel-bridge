private byte[] generateSecret(Context paramContext) {
	try {
		/* Get the public key used to sign the application. */
		paramContext = paramContext.getPackageManager().getPackageInfo(paramContext.getPackageName(), 64).signatures[0];

		/* Create a SHA1 hasher. */
		MessageDigest localMessageDigest = MessageDigest.getInstance("SHA1");

		/* Update the digest with the public key as a byte array. */
		localMessageDigest.update(paramContext.toByteArray());

		/* Convert the digest from a byte string to a hex string. */
		paramContext = generate(hex(localMessageDigest.digest())).getBytes("UTF-8");

		/* Return the secret. */
		return paramContext;
	} catch (Throwable paramContext) {
		Crashlytics.logException(paramContext);
	}

	return null;
}
