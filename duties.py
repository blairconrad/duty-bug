from duty import duty, tools


@duty
def test(ctx):
    ctx.run(
        tools.pytest("tests"), title="Run tests")


@duty
def format(ctx):
    ctx.run(tools.ruff(["format", "--check", "."]), title="Check format")
