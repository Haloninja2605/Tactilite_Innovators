# Accessible Learning for the Visually Impaired

This project is an accessible learning solution that bridges the gap between printed text and accessibility for visually impaired individuals. Our system uses Optical Character Recognition (OCR) and Artificial Intelligence (AI) to convert printed text into Braille, displayed through a tactile, pin-based mechanical box.

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Project Overview](#project-overview)
- [Key Components](#key-components)
- [System Benefits](#system-benefits)
- [Technical Specifications](#technical-specifications)
- [Implementation Plan](#implementation-plan)
- [Contributors](#contributors)

## Introduction
Visually impaired individuals face significant challenges in accessing written educational material. This project proposes a solution that transforms printed text into Braille, using a combination of OCR, AI, and physical components to enable users to read printed content through touch.

## Problem Statement
While there are digital and audio alternatives, Braille remains one of the most effective ways for visually impaired individuals to read and learn. However, converting printed materials to Braille can be costly and labor-intensive. This project aims to provide an affordable, real-time device that enables automatic conversion of text to Braille.

## Project Overview
The system operates in four stages:
1. **Text Recognition**: Using OCR, the system scans printed text from books or images and converts it into machine-readable text.
2. **AI-Based Text Processing**: An AI model classifies text into Braille-compatible letters, punctuation marks, and symbols.
3. **Braille Representation**: The text is translated into a binary matrix where each matrix represents a Braille character.
4. **Mechanical Display**: The binary matrix controls a set of unsharpened pins, arranged in a tactile box controlled by an Arduino system, allowing the user to feel the Braille characters.

## Key Components
- **Optical Character Recognition (OCR)**: Scans and converts printed text to digital form.
- **AI Processor**: Transforms text into Braille characters based on a predefined Braille code.
- **Pin Box**: A tactile device with unsharpened pins controlled by Arduino, allowing visually impaired users to feel Braille representations of text.
- **Binary Matrix**: A 2D array with `1` indicating a raised pin and `0` indicating a lowered pin, representing Braille characters.

## System Benefits
- **Immediate Braille Translation**: Real-time conversion of printed text to Braille.
- **Affordable**: Reduces the cost and effort associated with creating Braille materials.
- **User-Friendly**: Simple, intuitive pin-based system that allows tactile reading of printed content.

## Technical Specifications
- **OCR Software**: Google Tesseract or equivalent.
- **AI Model**: Trained on diverse datasets to accurately match text and Braille patterns.
- **Arduino**: Controls the pin box based on the binary matrix generated by the AI model.
- **Pins**: Safe, unsharpened pins raised or lowered through precision motors.

## Implementation Plan
1. **Phase 1**: Research and develop the AI model, and integrate it with the OCR system.
2. **Phase 2**: Build a prototype of the tactile pin box and conduct testing with various printed texts.

## Contributors
- Mridul Goyal
- Harsh Kamal
- Sumit Kumar
- Shreya Sen
- Preeti Bhargava
## Conclusion
This project has the potential to revolutionize learning accessibility for visually impaired individuals by converting printed text to Braille in real-time. We are eager to bring this project to life and contribute to educational accessibility.

---

Feel free to reach out for contributions or collaboration!
