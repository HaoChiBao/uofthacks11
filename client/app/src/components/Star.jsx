// Star.js

import React from 'react';
import styled from 'styled-components';

const StyledStar = styled.svg`
  z-index: 0;
  position: fixed;
  bottom: ${(props) => (props.bottom ? props.bottom : 0)};
  right: ${(props) => (props.right ? props.right : 0)};
  height: ${(props) => (props.height ? props.height : '100vh')};
  transform: ${(props) => (props.rotate ? `rotate(${props.rotate}deg)` : 'none')};
  width: 100%;
`;

const Star = ({ height, bottom, right, rotate }) => {
    return (
        <StyledStar viewBox="0 0 387 360" fill="none" xmlns="http://www.w3.org/2000/svg" height={height} bottom={bottom} right={right} rotate={rotate}>
            <path d="M309.574 0.893562L281.483 163.409L427.364 240.345L264.122 263.849L236.031 426.364L163.233 278.375L-0.00863265 301.879L118.242 186.913L45.4437 38.9234L191.324 115.86L309.574 0.893562Z" fill="#FFF8DC" />
        </StyledStar>
    );
};


export default Star;
