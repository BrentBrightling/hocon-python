class ConfigParseable(object):
    """
     * An opaque handle to something that can be parsed, obtained from
     * {@link ConfigIncludeContext}.
     *
     * <p>
     * <em>Do not implement this interface</em>; it should only be implemented by
     * the config library. Arbitrary implementations will not work because the
     * library internals assume a specific concrete implementation. Also, this
     * interface is likely to grow new methods over time, so third-party
     * implementations will break.
    """

    def parse(self, options):
        """
        ConfigObject parse(ConfigParseOptions options);

         * Parse whatever it is. The options should come from
         * {@link ConfigParseable#options options()} but you could tweak them if you
         * like.
         *
         * @param options
         *            parse options, should be based on the ones from
         *            {@link ConfigParseable#options options()}
        """
        raise NotImplementedError

    def origin(self):
        """
        ConfigOrigin origin();

         * Returns a {@link ConfigOrigin} describing the origin of the parseable
         * item.
        """
        raise NotImplementedError

    def options(self):
        """
        ConfigParseOptions options();

         * Get the initial options, which can be modified then passed to parse().
         * These options will have the right description, includer, and other
         * parameters already set up.
        """
        raise NotImplementedError
