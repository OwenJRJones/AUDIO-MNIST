import "./App.css";
import AudioRecorder from "./AudioRecorder";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

function App() {
	return (
		<QueryClientProvider client={queryClient}>
			<h1>Audio MNIST</h1>
			<p className="description">
				Say a digit from 0-9 and the network will return a prediction.
			</p>
			<AudioRecorder />
			<p className="foot-note">
				*Note: Please allow a few seconds for the first prediction to be produced.
			</p>
		</QueryClientProvider>
	);
}

export default App;
