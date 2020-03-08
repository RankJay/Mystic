import React, { Component } from 'react';
import backendsys from './ImpressiveWholeWheel/main.py' 
import {
  StyleSheet,
  Text,
  View,
  TextInput
} from 'react-native';

export default class App extends Component {

  constructor() {
    super()
    this.state = {
      inputFromUser: ""
    }
    this.input = this.input.bind(this)

    this.state = {
      outputFromUser: ""
    }
    this.output = this.output.bind(this)

    this.state = {
      languageFromUser: ""
    }
    this.language = this.language.bind(this)
  }

  input(newText) {
    this.setState({
      inputFromUser: newText
    })
  }
  
  output(newText) {
    this.setState({
      outputFromUser: newText
    })
  }

  language(newText) {
    this.setState({
      languageFromUser: newText
    })
  }

  render() {
    return (
      <View style={styles.container}>
        <Text>Enter your Input</Text>
        <TextInput 
          defaultValue={this.state.inputFromUser}
          onChangeText={this.input}
        />
        <Text>{this.state.inputFromUser}</Text>

        <Text>Enter your output</Text>
        <TextInput 
          defaultValue={this.state.outputFromUser}
          onChangeText={this.output}
        />
        <Text>{this.state.outputFromUser}</Text>

        <Text>Enter language of code</Text>
        <TextInput 
          defaultValue={this.state.languageFromUser}
          onChangeText={this.language}
        />
        <Text>{this.state.languageFromUser}</Text>
      </View>
    );
  }
}

function back(inputFromUser, outputFromUser, languageFromUser) {
  return backendsys(inputFromUser, outputFromUser, languageFromUser)
}

back(this.state.inputFromUser, this.state.outputFromUser, this.state.languageFromUser)

const styles = StyleSheet.create({
  container: {
    flex: 2,
    justifyContent: 'center',
    padding: 20
  }
})
