import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  ImageBackground,
  Dimensions,
  Image,
} from 'react-native';

const width_screen = Dimensions.get('window').width;

const card_item = width_screen - 35 * 2;

const card_size = {
  width: 320,
  height: 190,
};

const Card = (props) => {
  return (
    <ImageBackground
      source={require('../assets/card_visa_bg.png')}
      style={styles.card}>
      <View style={styles.cardIcon}>
        <Image source={require('../assets/card_icon.png')} />
      </View>
      <View style={styles.cardNumber}>
        <Text style={styles.cardNumberText}>{props.cardNumber}</Text>
      </View>
      <View style={styles.cardFooter}>
        <View>
          <Text style={styles.cardHolderName}>{props.cardHolder}</Text>
          <Text style={styles.cardName}>{props.cardName}</Text>
        </View>
        <Image source={require('../assets/visa_text.png')} />
      </View>
    </ImageBackground>
  );
};

export default Card;

const styles = StyleSheet.create({
  card: {
    width: card_item,
    height: (card_item * card_size.height) / card_size.width,
    padding: 24,
  },
  cardNumber: {
    flex: 1,
    justifyContent: 'center',
  },
  cardNumberText: {
    color: 'white',
    fontSize: 15,
    fontWeight: 'bold',
  },
  cardHolderName: {color: 'rgba(255,255,255,0.7)'},
  cardName: {color: 'white', fontSize: 15},
  cardFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
});
