module.exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: "Use me for the Strangler Pattern",
    }),
  };
};
